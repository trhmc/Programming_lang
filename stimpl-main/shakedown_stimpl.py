from stimpl import *



if __name__=='__main__':
  ## Make sure that sequences work in the proper order (10 pts)
  # i = 0
  # j = (i = i + 1)
  # k = (i = i + 1)
  # l = (i = i + 1)
  program = Program(\
      Assign(Variable("i"), IntLiteral(0)),\
      Assign(Variable("j"), Assign(Variable("i"), Add(Variable("i"), IntLiteral(1)))),\
      Assign(Variable("k"), Assign(Variable("i"), Add(Variable("i"), IntLiteral(1)))),\
      Assign(Variable("l"), Assign(Variable("i"), Add(Variable("i"), IntLiteral(1)))),\
    )
  run_value, run_type, run_state = run_stimpl(program)
  check_equal((1, Integer()), run_state.get_value("j"))
  check_equal((2, Integer()), run_state.get_value("k"))
  check_equal((3, Integer()), run_state.get_value("l"))
  check_equal((3, Integer()), run_state.get_value("i"))
  ## Make sure that While loops work! (10 pts)
  program = Program(\
      Assign(Variable("j"), IntLiteral(0)),\
      While(Lt(Variable("j"), IntLiteral(10)),\
        Sequence(\
          Assign(Variable("j"), Add(Variable("j"), IntLiteral(1))),\
          )\
        )\
      )
  run_value, run_type, run_state = run_stimpl(program)
  check_equal((10, Integer()), run_state.get_value("j"))