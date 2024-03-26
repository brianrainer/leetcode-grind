def solve(n,m,q,p_dict,v_dict,v_p_dict):
    return ["A", "B"]


def fast():
    import io,os,sys
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    n, m, q = [int(x) for x in input().strip().split()]
    p_dict = {}
    v_dict = {}
    v_p_dict = {}

    for i in range(n):
        name, cap, pos = input().split()
        p_dict[i] = (name, int(cap), int(pos))
    
    for i in range(m):
        vi, vpos = [int(x) for x in input().split()]
        v_dict[vi] = vpos
    
    for i in range(q):
        vi2, pname, vcap = input().split()
        v_p_dict[vi2] = (pname, vcap)
    
    res = solve(n,m,q,p_dict,v_dict,v_p_dict)
    sys.stdout.write(str(len(res)) + "\n")
    sys.stdout.write(str(" ".join(res)) + "\n")

fast()
