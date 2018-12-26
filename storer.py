from models import Program


def store(programs):
    for program in programs:
        if Program.get(Program.kofa_id == program['kofa_id']) is None:
            Program.create(**program)
