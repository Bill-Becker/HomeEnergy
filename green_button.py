import pandas as pd
import xml.etree.ElementTree as ET
from greenbutton_objects import parse

file_path = "XCEL_Electric_15_Minute_01-01-2023_01-01-2024.xml"

object = parse.parse_feed(file_path)

dummy = 1