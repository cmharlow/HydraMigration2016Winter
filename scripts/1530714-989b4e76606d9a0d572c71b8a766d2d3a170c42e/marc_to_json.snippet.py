def marc_to_dict(marcobj):
    control_fields = ('001', '002', '003', '004', '005', '006', '007', '008', '009')
    jsonobj = {}
    jsonobj['leader'] = marcobj.leader
    jsonobj['fields'] = []
    for field in marcobj.fields:
        if field.tag in control_fields:
            jsonobj['fields'].append( { field.tag : re.escape(field.data) } )
        else:
            subdict = {}
            subdict[field.tag] = {}
            it = iter(field.subfields)
            subdict[field.tag]['subfields'] = [ { k : re.escape(v) } for k, v in zip(it, it) ]
            subdict[field.tag]['ind1'] = field.indicator1
            subdict[field.tag]['ind2'] = field.indicator2

            jsonobj['fields'].append(subdict)

    return jsonobj

def marc_to_json(marcobj):
    """ http://dilettantes.code4lib.org/blog/2010/09/a-proposal-to-serialize-marc-in-json/
    """
    return json.dumps(marc_to_dict(marcobj))


