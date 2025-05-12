import sys 


def main():
    coordinate_list = [41.22 , -71.118]
    coordinate_tuble = (41.22 , -71.117)
    
    print(f'{sys.getsizeof(coordinate_list)} bytes')
    print(f'{sys.getsizeof(coordinate_tuble)} bytes')


main()    