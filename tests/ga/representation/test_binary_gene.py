# Local Module
from ga.representation.binary import BinaryGeneOperator, BinaryRepresentation

REPRS = [BinaryRepresentation(0, 1, 4), BinaryRepresentation(0, 1, 4)]
SUBJECT = BinaryGeneOperator(REPRS)


def test_generate():
    gene = SUBJECT.generate()
    assert len(gene) == 28
    assert len(gene) == SUBJECT.length


def test_encode():
    # Subject tuple is the 'max' of obj_func
    gene = SUBJECT.encode((0.6887, 0.9866))
    assert isinstance(gene, str)
    assert gene == '0110101110011110011010001010'


def test_decode():
    # Subject gene is the 'min' of obj_func
    phenotype = SUBJECT.decode('0000000000000100000000000010')
    assert isinstance(phenotype, tuple)
    assert phenotype == (0.0001, 0.0002)


def test_encode_wrong_len():
    gene = SUBJECT.encode((0.99, 0.2, 0.6))
    assert gene == ''


def test_decode_wrong_len():
    phenotype = SUBJECT.decode('010')
    assert phenotype == ()


def test_crossover():
    first = '1011'
    second = '1000'

    first, second = SUBJECT.crossover(first, second, 3)
    assert first == '1010'
    assert second == '1001'


def test_mutation():
    gene = '0000'

    subject = SUBJECT.mutation(gene, 2)
    assert subject == '0010'


def test_valid_by_gene():
    gene = '1' * SUBJECT.length
    valid = SUBJECT.valid_gene(gene)
    assert valid == False

    gene = '0' * SUBJECT.length
    valid = SUBJECT.valid_gene(gene)
    assert valid == True
