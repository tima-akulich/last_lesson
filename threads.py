from threading import Thread


def foo_print_a(n):
    for i in range(n):
        print('A')


def foo_print_b(n):
    for i in range(n):
        print('B')


if __name__ == '__main__':

    foo_print_a(10)
    foo_print_b(10)

    print('/' * 30)

    thread1 = Thread(target=foo_print_a, args=(10, ))
    thread2 = Thread(target=foo_print_b, args=(10, ))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()


    class MyThread(Thread):
        def run(self):
            print('Run my thread')

    my_thread = MyThread()
    my_thread.start()
