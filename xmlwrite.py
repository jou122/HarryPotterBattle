import xml.etree.ElementTree as ET
import os


script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "Output.xml" # Relative path
abs_file_path = os.path.join(script_dir, rel_path) # Absoulte path

 
# This is the parent (root) tag
# onto which other tags would be
# created
data = ET.Element('chess\n')
data2 = ET.Element('chess\n')
 
# Adding a subtag named `Opening`
# inside our root tag
element1 = ET.SubElement(data, 'Opening\n')
element1_2 = ET.SubElement(data2, 'Opening\n')
# Adding subtags under the `Opening`
# subtag
s_elem1 = ET.SubElement(element1, 'E4\n')
s_elem2 = ET.SubElement(element1, 'D4\n')
s_elem1_2 = ET.SubElement(element1_2, 'E4\n')
s_elem2_2 = ET.SubElement(element1_2, 'D4\n')
# Adding attributes to the tags under
# `items`
s_elem1.set('type', 'Accepted\n')
s_elem2.set('type', 'Declined\n')
s_elem1_2.set('type', 'Accepted\n')
s_elem2_2.set('type', 'Declined\n')
# Adding text between the `E4` and `D5`
# subtag
s_elem1.text = "King's Gambit Accepted\n"
s_elem2.text = "Queen's Gambit Declined\n"
s_elem1_2.text = "King's Gambit Accepted\n"
s_elem2_2.text = "Queen's Gambit Declined\n"
# Converting the xml data to byte object,
# for allowing flushing data to file
# stream

b_xml = ET.tostring(data, encoding='unicode', method='xml')

b_xml2= ET.tostring(data2, encoding='unicode', method='xml')

# Opening a file under the name `items2.xml`,
# with operation mode `wb` (write + binary)
with open(abs_file_path, "w") as f:
    f.write(b_xml+"\n\n\n"+b_xml2)

 



