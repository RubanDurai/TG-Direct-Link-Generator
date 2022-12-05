

with open('main/template/req.html') as r:
    heading = 'Watch {}'.format("Test Name")
    tag ="Video"
    html = (r.read()).replace('tag', tag).format()