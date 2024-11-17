class Pretty:
    def __init__(self, obj):
        self.obj = obj

    def _repr_html_(self):
        try:
            return self.to_html(*self.format())
        except NotImplementedError:
            return str(self.obj)

    def format(self):
        if isinstance(self.obj, list):
            if all(isinstance(element, dict) for element in self.obj):
                keys = []
                for d in self.obj:
                    for i, key in enumerate(d):
                        if key not in keys:
                            before = next(
                                (k for k in list(d.keys())[i:] if k in keys), None
                            )
                            if before:
                                keys.insert(keys.index(before), key)
                            else:
                                keys.append(key)
                return (
                    [keys] + [[d.get(key) for key in keys] for d in self.obj],
                    True,
                    False,
                )
            else:
                return self.obj, False, False
        elif isinstance(self.obj, dict):
            return (
                [
                    [key] + (value if isinstance(value, (list, tuple)) else [value])
                    for key, value in self.obj.items()
                ],
                False,
                True,
            )
        raise NotImplementedError()

    def to_html(self, values, header_row=False, header_col=False):
        if not all(isinstance(value, (list, tuple)) for value in values):
            values = [values]
        html = ["<table>"]
        for index_row, value in enumerate(values):
            html.append("<tr>")
            if not isinstance(value, (list, tuple)):
                value = [value]
            for index_col, el in enumerate(value):
                if (header_row and index_row == 0) or (header_col and index_col == 0):
                    node = "th"
                else:
                    node = "td"
                html.append("<{0}>{1}</{0}>".format(node, str(el)))
            html.append("</tr>")
        html.append("</table>")
        return "".join(html)
