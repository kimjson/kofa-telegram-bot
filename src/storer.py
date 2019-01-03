from models import Program


def store(program_dicts):
    return (Program.insert_many(program_dicts)
                   .on_conflict_replace()
                   .returning(Program)
                   .execute())
