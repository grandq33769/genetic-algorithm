# Third Party Library
import pytest

# Local Module
from ga.representation.binary import BinaryRepresentation

SUBJECT = BinaryRepresentation(4.7, 5.4, 1)


def test_generate():
    chromosome = SUBJECT.generate()
    assert isinstance(chromosome, str)
    assert len(chromosome) == 3


def test_decode():
    phenotype = SUBJECT.decode('010')
    assert phenotype == 4.9


def test_encode():
    chromosome = SUBJECT.encode(4.9)
    assert chromosome == '010'


def test_long_decimal():
    subject = BinaryRepresentation(4.79, 5.43, 5)
    chromosome = subject.generate()
    assert isinstance(chromosome, str)
    assert len(chromosome) == 16

    phenotype = subject.decode('00000011011000001')
    assert phenotype == 4.80729


def test_fail():
    with pytest.raises(ValueError):
        subject = BinaryRepresentation(5.4, 4.7, 2)
