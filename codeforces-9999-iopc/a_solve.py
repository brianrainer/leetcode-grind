def solve(s):
    sl = s.strip().split('@')
    if len(sl) != 2:
        return 'no'
    name, odoocom = sl
    ol = odoocom.strip().split('.')
    if len(ol) != 2:
        return 'no'
    if ol[0] != 'odoo':
        return 'no'
    if ol[1] != 'com':
        return 'no'
    if len(name) < 2:
        return 'no'
    if len(name) > 4:
        return 'no'
    for ch in name:
        if ch not in "abcdefghijklmnopqrstuvwxyz":
            return 'no'
    return 'yes'


def fast():
    import io,os,sys
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    s = input().decode()
    sys.stdout.write(str(solve(s)) + "\n")

fast()