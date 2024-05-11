from contextlib import contextmanager


@contextmanager
def get_conn():
    conn = 'snowflake'
    print('before')
    yield conn
    print('after')


def main():
    with get_conn() as connection:
        print(connection)


if __name__ == '__main__':
    main()
