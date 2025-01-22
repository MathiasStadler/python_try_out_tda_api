#!/home/trapapa/python_try_out_tda_api/.venv/bin/python3
from tda.scripts.orders_codegen import latest_order_main

if __name__ == '__main__':
    import sys
    sys.exit(latest_order_main(sys.argv[1:]))
