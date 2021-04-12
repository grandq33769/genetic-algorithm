# Third Party Library
import pytest

# Local Module
from ga.representation.float import FloatRepresentation

SUBJECT = FloatRepresentation(4.7, 5.4, 3)


def test_generate():
    chromosome = SUBJECT.generate()
    assert isinstance(chromosome, float)


def test_decode():
    phenotype = SUBJECT.decode(4.99001)
    assert phenotype == 4.99


def test_fail():
    with pytest.raises(ValueError):
        subject = FloatRepresentation(5.4, 4.7, 2)
