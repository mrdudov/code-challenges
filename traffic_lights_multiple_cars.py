def traffic_lights(road, n):

    result = []
    result.append(road)

    road_l = road.split()
    g_tl_live_cycle = 'G'*5 + 'O' + 'R'*5
    o_tl_live_cycle = 'O' + 'R'*5 + 'G'*5
    r_tl_live_cycle = 'R'*5 + 'G'*5 + 'O'

    init_tl = [i if i in 'GOR' else 0 for i in road]

    tl_n = ['.']*len(road)
    for m in range(n):
        for i, tl in enumerate(init_tl):
            if tl == 'G':
                tl_n[i] = g_tl_live_cycle[m+1 % 11]
            if tl == 'O':
                tl_n[i] = o_tl_live_cycle[m+1 % 11]
            if tl == 'R':
                tl_n[i] = r_tl_live_cycle[m+1 % 11]
        result.append(''.join(tl_n))

    return result
