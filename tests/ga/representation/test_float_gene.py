# Local Module
from ga.representation.float import FloatGeneOperator, FloatRepresentation

REPRS = [FloatRepresentation(0, 1, 4), FloatRepresentation(0, 1, 4)]
SUBJECT = FloatGeneOperator(REPRS)


def test_generate():
    gene = SUBJECT.generate()
    assert len(gene) == 2
    assert len(gene) == SUBJECT.length


def test_decode():
    # Subject gene is the 'min' of obj_func
    phenotype = SUBJECT.decode((0.0001, 0.0002))
    assert isinstance(phenotype, tuple)
    assert phenotype == (0.0001, 0.0002)


def test_decode_wrong_len():
    phenotype = SUBJECT.decode((0, 3, 5))
    assert phenotype == ()


def test_crossover():
    first = (0.002, 0.005)
    second = (0.1034, 0.8945)

    first, second = SUBJECT.crossover(first, second, 1)
    assert first == (0.002, 0.8945)
    assert second == (0.1034, 0.005)


def test_mutation():
    gene = (0.3567, 0.2257)

    subject = SUBJECT.mutation(gene, 0)
    assert isinstance(subject, tuple)
    assert isinstance(subject[0], float)
    assert subject[1] == 0.2257


def test_valid_by_gene():
    gene = (3.5, 4.8)
    valid = SUBJECT.valid_gene(gene)
    assert valid == False

    gene = (0.005, 0.2267)
    valid = SUBJECT.valid_gene(gene)
    assert valid == True
