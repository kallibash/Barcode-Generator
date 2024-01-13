import barcode

from barcode import EAN13

from barcode.writer import ImageWriter

data = "602358647511"

code = EAN13(data, writer=ImageWriter())

code.writer.set_options({"module_width": 0.2, "module_height": 15})

code.save('new_barcode')
