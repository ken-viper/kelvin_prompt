import time
import torch
import re
from typing import List
from prompting.rewards import BaseRewardModel, BatchRewardOutput, RewardModelTypeEnum


class FloatDiffModel(BaseRewardModel):
    @property
    def name(self) -> str:
        return 'float_diff'

    @property
    def model_type(self) -> RewardModelTypeEnum:
        return RewardModelTypeEnum.WEIGHTED_REWARD

    def __init__(self, **kwargs):
        super().__init__()

    def math_score(self, reference, completion):
        # Extract all the digits and . from the completion and take only the last one
        #TODO: More flexible regex which catches rational fractions and scientific notation
        # for loop over all words reversed and try to cast as a float, break when you find the first one

        for word in completion.split()[::-1]:
            try:
                # Convert the string to a float                
                completion_digits = float(word)
                # this is okay beccause we already checked that the reference is a float
                reference = float(reference)
                # Convert the reference to a float
                if completion_digits == reference:
                    return 1.0
                # Compute the difference
                diff = abs(reference - completion_digits)/(reference + 1e-6)
                # Make sure the difference is between 0 and 1
                diff = min(abs(diff), 1)
                return 1.0 - diff                
                
            except ValueError:
                continue
            
        return 0.0

    def reward(self, reference: str, completions: List[str]) -> BatchRewardOutput:
        """Compute difference scores given a completion and reference pair."""
        rewards = []
        timings = []

        for completion in completions:
            t0 = time.time()
            reward = self.math_score(reference, completion) 
            timings.append(time.time() - t0)
            rewards.append(reward)

        output = BatchRewardOutput(
            rewards = torch.FloatTensor(rewards),
            timings = torch.FloatTensor(timings),
            extra_info = {'type': 'math', },
        )
        return output
