import taichi as ti

@ti.all_archs
def test_offload_with_cross_block_locals():
  ti.cfg.print_ir = True
  ret = ti.var(ti.f32)

  @ti.layout
  def place():
    ti.root.place(ret)


  @ti.kernel
  def ker():
    s = 0
    for i in range(10):
      s += i
    ret[None] = s

  ker()

  assert ret[None] == 45