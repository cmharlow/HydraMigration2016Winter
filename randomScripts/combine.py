import xml.dom.pulldom
import xml.dom.minidom
import codecs
import os


def main():
    ofile = codecs.lookup('utf-8')[-1](file('output.xml', 'wb'))

    ofile.write('<?xml version="1.0" encoding="UTF-8"?><COLL>')

    xmldir = "DLXSexports/Server/chla_xml/serials/"

    recordCount = 0

    for subdir, dirs, files in os.walk(xmldir):
        for xmlfile in files:
            events = xml.dom.pulldom.parse(xmldir + xmlfile)
            for (event, node) in events:
                if event == "START_ELEMENT" and node.tagName == 'DLPSTEXTCLASS':
                    events.expandNode(node)
                    node.writexml(ofile)
                    recordCount += 1

    ofile.write('\n</COLL>'), ofile.close()

    print("Wrote out %d records" % recordCount)

if __name__ == '__main__':
    main()
