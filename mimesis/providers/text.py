# -*- coding: utf-8 -*-

"""Provides data related to text."""

from typing import Any, Final, List, Tuple

from mimesis.data import SAFE_COLORS
from mimesis.providers.base import BaseDataProvider

__all__ = ["Text"]


class Text(BaseDataProvider):
    """Class for generating text data."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize attributes.

        :param locale: Current locale.
        :param seed: Seed.
        """
        super().__init__(*args, **kwargs)
        self._datafile = "text.json"
        self._load_datafile(self._datafile)

    class Meta:
        """Class for metadata."""

        name: Final[str] = "text"

    def alphabet(self, lower_case: bool = False) -> List[str]:
        """Get an alphabet for current locale.

        :param lower_case: Return alphabet in lower case.
        :return: Alphabet.
        """
        case = "uppercase" if not lower_case else "lowercase"

        alpha: List[str] = self.extract(["alphabet", case])
        return alpha

    def level(self) -> str:
        """Generate a random level of danger or something else.

        :return: Level.

        :Example:
            critical.
        """
        levels: List[str] = self.extract(["level"])
        return self.random.choice(levels)

    def text(self, quantity: int = 5) -> str:
        """Generate the text.

        :param quantity: Quantity of sentences.
        :return: Text.
        """
        text = ""
        for _ in range(quantity):
            text += " " + self.random.choice(self.extract(["text"]))
        return text.strip()

    def sentence(self) -> str:
        """Get a random sentence from text.

        :return: Sentence.
        """
        return self.text(quantity=1)

    def title(self) -> str:
        """Get a random title.

        :return: The title.
        """
        return self.text(quantity=1)

    def words(self, quantity: int = 5) -> List[str]:
        """Generate lis of the random words.

        :param quantity: Quantity of words. Default is 5.
        :return: Word list.

        :Example:
            [science, network, god, octopus, love]
        """
        words = self.extract(["words", "normal"])
        words_list = [self.random.choice(words) for _ in range(quantity)]
        return words_list

    def word(self) -> str:
        """Get a random word.

        :return: Single word.

        :Example:
            Science.
        """
        return self.words(quantity=1)[0]

    def swear_word(self) -> str:
        """Get a random swear word.

        :return: Swear word.

        :Example:
            Damn.
        """
        words: List[str] = self.extract(["words", "bad"])
        return self.random.choice(words)

    def quote(self) -> str:
        """Get a random quote.

        :return: Quote from movie.

        :Example:
            "Bond... James Bond."
        """
        quotes: List[str] = self.extract(["quotes"])
        return self.random.choice(quotes)

    def color(self) -> str:
        """Get a random name of color.

        :return: Color name.

        :Example:
            Red.
        """
        colors: List[str] = self.extract(["color"])
        return self.random.choice(colors)

    @staticmethod
    def _hex_to_rgb(color: str) -> Tuple[int, ...]:
        """Convert hex color to RGB format.

        :param color: Hex color.
        :return: RGB tuple.
        """
        if color.startswith("#"):
            color = color.lstrip("#")
        return tuple(int(color[i : i + 2], 16) for i in (0, 2, 4))

    def hex_color(self, safe: bool = False) -> str:
        """Generate a random hex color.

        :param safe: Get safe Flat UI hex color.
        :return: Hex color code.

        :Example:
            #d8346b
        """
        if safe:
            return self.random.choice(SAFE_COLORS)

        return "#{:06x}".format(self.random.randint(0x000000, 0xFFFFFF))

    def rgb_color(self, safe: bool = False) -> Tuple[int, ...]:
        """Generate a random rgb color tuple.

        :param safe: Get safe RGB tuple.
        :return: RGB tuple.

        :Example:
            (252, 85, 32)
        """
        color = self.hex_color(safe)
        return self._hex_to_rgb(color)

    def answer(self) -> str:
        """Get a random answer in current language.

        :return: An answer.

        :Example:
            No
        """
        answers: List[str] = self.extract(["answers"])
        return self.random.choice(answers)
