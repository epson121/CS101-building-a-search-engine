def stamps(goal):
    p5 = 0;
    p2 = 0;
    p1 = 0;
    sum = 0;
    if goal > 5:
        while sum < goal:
            sum = sum + 5;
            p5 = p5 + 1;
            x = sum + 5;
            if x > goal:
                break;
    if goal > 2:
        while sum < goal:
            sum = sum + 2;
            p2 = p2 + 1;
            z = sum +2;
            if z > goal:
                break;
    while sum < goal:
        sum = sum + 1;
        p1 = p1 +1;
    return p5, p2, p1;

print stamps(3);  
