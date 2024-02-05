from scr_zillo import Data_zillo
from fill_forme import Fill_form

data = Data_zillo()
fill_it = Fill_form()
data.get_data()
dict_data = data.data_dict
fill_it.fill(dict_data)
fill_it.quit()

