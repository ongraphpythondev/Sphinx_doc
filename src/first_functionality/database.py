"""
Database Functionalities
------------------------
Database is very crutial thing in and project
"""

class Databse:
    """
    Database class is responsible for connecting with database
    """

    def __init__(self , connection_string):
        """
        this connection string is used to connect with sql server
        :param connection_string : str
        """
        self.connection_string = connection_string

    
    def connect(self , username : str , password : str , port : int) -> str:
        """
        this method is used to connect database
        :param username : str
        :param password : str
        :param port : int

        :return:str
        """
        return f"this is run on port no.{port}"