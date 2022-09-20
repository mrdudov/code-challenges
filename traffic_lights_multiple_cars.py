def traffic_lights(road, n):
    
    result = []
    result.append(road)
    
    g_tl_live_cycle = 'G'*5 + 'O' + 'R'*5
    o_tl_live_cycle = 'O' + 'R'*5 + 'G'*5
    r_tl_live_cycle = 'R'*5 + 'G'*5 + 'O'
    
    init_tl = [i if i in 'GOR' else 0 for i in road]
    
    tl_n = ['.']*len(road)
    car_n = list([c if c == 'C' else '.' for c in road])
    
    for m in range(1, n+1):
        for i, tl in enumerate(init_tl):
            if tl == 'G':
                tl_n[i] = g_tl_live_cycle[m%11]
            if tl == 'O':
                tl_n[i] = o_tl_live_cycle[m%11]    
            if tl == 'R':
                tl_n[i] = r_tl_live_cycle[m%11]
        
        
        for i in range(len(car_n) -1, -1, -1):
            try:
                is_tl_g = tl_n[i+1] not in 'OR'
            except:
                is_tl_g = True
            try:
                is_roar_free = car_n[i+1] == '.'
            except:
                is_roar_free = True
            try:
                last = True
                if tl_n[i+1] == 'G' and car_n[i+2] == 'C':
                    last = False
            except:
                last = True

            if car_n[i] == 'C' and is_tl_g and is_roar_free and last:
                try:
                    car_n[i] = '.'
                    car_n[i+1] = 'C'
                except:
                    car_n[i] = '.'
            
        result.append(''.join([car_n[i] if car_n[i] in 'C' else tl_n[i] for i in range(len(car_n))]))
    
    return result
