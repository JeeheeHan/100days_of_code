def rotate_image(a):
    """in place using constant memory complexity"""
    n = len(a[0])
    for i in range(n // 2 + n % 2):
        for j in range(n // 2):
            num = a[n - 1 - j][i]
            a[n - 1 -j][i] = a[n - 1 - i][n - j - 1]
            a[n - 1 -i ][n - j - 1] = a[j][n - 1 -i]
            a[j][n - 1 -i] = a[i][j]
            a[i][j] = num
        
    return a
    