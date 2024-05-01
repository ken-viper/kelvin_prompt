import random
from .base import ChallengeTemplate


class MathChallengeTemplate(ChallengeTemplate):
    def __init__(self):
        super().__init__()
        self.templates = [
            "{greeting}{greeting_punctuation}{query}{whitespace}{request}<end>",
            "{query}<end>{greeting}{greeting_punctuation}{request}{whitespace}",
            "{greeting}{greeting_punctuation}{query}<end>{request}{whitespace}",
            "{query}{whitespace}{request}<end>{greeting}{greeting_punctuation}",
        ]
        self.fields = {
            "greeting": [
                "Hello",
                "Hi",
                "Hey",
                "Yo",
                "What's up",
                "Howdy",
                "Hola",
                "Bonjour",
                "G'day",
                "Good morning",
                "Good afternoon",
                "Good evening",
                "Greetings",
                "Sup",
                "Hi there",
                "Hey there",
                "Morning",
                "Afternoon",
                "Evening",
                "Salutations",
                "Hey, what's going on",
                "Howdy",
                "Sup",
                "Sup yo",
                "Yo",
                "Yo yo",
                "Greetings",
                "Greetings to you",
                "Hello",
                "Hello friend",
                "Hello to you",
                "Hey",
                "Hey there",
                "",
            ],
            "greeting_punctuation": [
                "!",
                "! ",
                "!  ",
                "!\n",
                ",",
                ", ",
                ",  ",
                ",\n",
                ".",
                ". ",
                ".  ",
                ".\n",
                "",
                " ",
                "  ",
                "\n",
                "...",
                "... ",
                "...  ",
                "...\n",
                "",
            ],
            "request": [
                "Can you assist me, please?",
                "Could you lend me a hand?",
                "Would you mind helping me out?",
                "I could use some assistance.",
                "Do you have a moment to help me?",
                "I'm in need of some help.",
                "Could you give me a hand with this?",
                "Would you be willing to help me?",
                "Can you offer me some guidance?",
                "I'm struggling a bit, could you help?",
                "I could really use your expertise.",
                "Would you mind showing me how to do this?",
                "Can you lend me your expertise for a moment?",
                "I'm having trouble, could you assist?",
                "Would you be able to lend me a hand?",
                "Can you offer me some assistance?",
                "I'm stuck, could you help me out?",
                "Could you assist me with this problem?",
                "Would you be so kind as to help me?",
                "Can you offer me some help, please?",
                "Solve",
                "Could you spare a moment to help me?",
                "Would you mind giving me some assistance?",
                "Can you help me understand this better?",
                "I need your help with something.",
                "Could you offer me some support, please?",
                "Would you be willing to give me a hand?",
                "Can you show me how to do this?",
                "I'm having difficulty, could you help me?",
                "Could you assist me with this issue?",
                "Would you mind helping me with this task?",
                "Can you provide some help, please?",
                "I'm in a bit of a bind, could you help?",
                "Could you lend me a hand with this problem?",
                "Would you be able to offer me some guidance?",
                "Can you help me out with this, please?",
                "I'm having trouble understanding, could you help?",
                "Could you offer me some assistance, please?",
                "Would you mind assisting me with this?",
                "Can you give me some advice?",
                "I could use your help with this.",
                "Could you spare some time to help me?",
                "Would you be willing to lend me a hand?",
                "Can you help me solve this problem?",
                "I'm struggling to figure this out, could you help?",
                "Could you provide me with some assistance?",
                "Would you mind showing me what to do?",
                "Can you assist me in resolving this issue?",
                "I could really use your help.",
                "Could you help me out with this task?",
                "Would you be so kind as to give me a hand?",
                "Can you help me with this problem, please?",
                "I'm stuck on this, could you assist?",
                "Could you lend me a hand with this, please?",
                "Would you be able to provide me with some guidance?",
                "Can you offer me some assistance with this?",
                "I'm having difficulty understanding, could you help me?",
                "Could you assist me with this problem, please?",
                "Would you mind giving me a hand with this?",
                "Can you show me how to do this, please?",
                "I'm struggling with this, could you help me out?",
                "Could you offer me some help with this?",
                "Would you be willing to help me with this, please?",
                "Can you provide me with some support, please?",
                "I'm in a bit of a bind, could you assist me?",
                "Could you lend me your expertise?",
                "Would you be able to spare a moment to help me?",
                "Can you help me out with this problem, please?",
                "I'm having trouble with this, could you help me out?",
                "Could you assist me with this task, please?",
                "Would you mind offering me some assistance?",
                "Can you assist me with this issue, please?",
                "I could use some assistance with this, could you help?",
                "Could you give me a hand with this issue, please?",
                "Would you be so kind as to lend me a hand?",
                "Can you provide me with some assistance on this?",
                "I'm having difficulty with this task, could you help?",
                "Could you offer me some help on this, please?",
                "Would you mind helping me with this problem?",
                "Can you lend me a hand with this, please?",
                "I'm stuck on this problem, could you help?",
                "Could you show me how to do this, please?",
                "Would you be willing to assist me with this?",
                "Can you help me with this task, please?",
                "I'm struggling with this problem, could you assist?",
                "Could you give me some guidance on this, please?",
                "Would you mind giving me some help with this?",
                "Can you help me with this issue, please?",
                "I could use your help with this problem.",
                "Could you spare some time to help me out?",
                "Would you be able to lend me your expertise?",
                "Can you offer me some assistance with this problem?",
                "I'm in need of some help with this, could you assist?",
                "Could you assist me with this problem, please?",
                "Can you help me out with this issue, please?",
                "I'm having trouble with this task, could you help?",
                "Could you lend me a hand with this problem, please?",
                "Would you be willing to give me some assistance?",
                "Can you provide me with some help, please?",
                "I'm stuck on this issue, could you help me?",
                "Could you show me what to do, please?",
                "Would you mind helping me with this task, please?",
                "Can you lend me your expertise for a moment, please?",
                "I'm struggling with this issue, could you assist me?",
                "Could you give me a hand with this problem, please?",
                "Would you be so kind as to offer me some assistance?",
                "Can you help me understand this, please?",
                "I could use your help figuring this out.",
            ],
            "whitespace": [
                "",
                " ",
                " ",
                "\n",
                "\n\n",
            ]
        }