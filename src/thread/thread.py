from threading import Thread, ThreadError


class Threads:

    """
    Thread managment class
    """

    def __init__(self):
        self.__threads = []

    def start(self, func, args: tuple, _id: int) -> bool:
        """
        Create and start new thread.

        :param func: function to start
        :type func: function
        :param args: function args
        :type args: tuple
        :param _id: thread id
        :type _id: int
        :returns: True if thread started successfully otherwise False
        :rtype: bool
        """
        try:
            proc = Thread(target=func, args=args, daemon=True)
            proc.start()
            self.__threads.append((_id, proc))
            return True
        except ThreadError as thErr:
            print(f"Error while starting new thread:\n\t{thErr}")
            return False

    def join_by_id(self, _id: int):
        """
        Join thread by id. 

        :param _id: thread id
        :type _id: int
        """
        try:
            for _idn, thread in self.__threads:
                if _idn == _id:
                    thread.join()
                    break
        except ThreadError as joinErr:
            print(f"Error while joining thread:\n\tID: {_id}\n\t{joinErr}")
            exit(1)

    def join_all(self):
        """ 
        Join all threads.
        """
        try:
            for _id, thread in self.__threads:
                thread.join()
        except ThreadError as joinErr:
            print(f"Error while joining threads:\n\t{joinErr}")
            exit(1)
