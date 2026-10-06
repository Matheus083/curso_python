class Foo:
    def __init__(self, x):
        """Construtor da classe Foo

        :param x: Um valor qualquer
        :type x: int or float
        """
        self.x = x

    def bar(self):
        """Método bar

        Este método deve ser implementado por subclasses.
        :raises NotImplementedError: Se o método não for implementado por subclasses
        """
        raise NotImplementedError("This method should be implemented by subclasses.")