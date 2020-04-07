from threading import Thread, ThreadError


class Threads(): 

    """
    Thread managment class
    """

    def __init__(self): 
        self.__threads = []

    def start(self, func, args: tuple) -> bool: 
        """
        Create and start new thread.

        :param func: function to start
        :type func: function
        :param args: function args
        :type args: tuple
        :returns: True if thread started successfully otherwise False
        :rtype: bool
        """
        try: 
            proc = Thread(target=func, args=args, daemon=True)
            proc.start()
            self.__threads.append(proc)
            return True
        except ThreadError as thErr: 
            print(f"Error while starting new thread:\n\t{thErr}")
            return False

    def join_all(self): 
        """ 
        Join all threads.
        """
        try: 
            for thread in self.__threads: 
                thread.join()
        except ThreadError as joinErr: 
            print(f"Error while joining threads:\n\t{joinErr}")
            exit(1)
