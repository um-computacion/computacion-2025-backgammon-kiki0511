import unittest
from core.exceptions import BackgammonError
from core.exceptions import MovimientoInvalidoError
from core.exceptions import PuntoInvalidoError
from core.exceptions import ValorDadoInvalidoError
from core.exceptions import JuegoTerminadoError
from core.exceptions import TurnoIncorrectoError
from core.exceptions import FichaEnBarraError
from core.exceptions import BearOffInvalidoError


class TestExceptions(unittest.TestCase):
    """
    Clase de pruebas para las excepciones del juego.
    
    Recibe: Nada
    Hace: Prueba todas las clases de excepciones
    Devuelve: Nada
    """
    
    def test_backgammon_error(self):
        """
        Prueba la excepcion BackgammonError.
        
        Recibe: Nada
        Hace: Verifica que se puede crear y lanzar
        Devuelve: Nada
        """
        # crear la excepcion con un mensaje
        mensaje_prueba = "mensaje de prueba"
        error = BackgammonError(mensaje_prueba)
        
        # verificar que se creo
        resultado_none = (error == None)
        self.assertEqual(resultado_none, False)
        
        # verificar el mensaje
        mensaje_obtenido = str(error)
        self.assertEqual(mensaje_obtenido, "mensaje de prueba")
        
        # probar lanzar la excepcion
        error_capturado = False
        try:
            raise BackgammonError("error lanzado")
        except BackgammonError as e:
            error_capturado = True
            mensaje_error = str(e)
            self.assertEqual(mensaje_error, "error lanzado")
        
        # verificar que se capturo el error
        self.assertEqual(error_capturado, True)
        
        # crear sin mensaje
        error2 = BackgammonError()
        resultado_none2 = (error2 == None)
        self.assertEqual(resultado_none2, False)
    
    def test_movimiento_invalido_error(self):
        """
        Prueba la excepcion MovimientoInvalidoError.
        
        Recibe: Nada
        Hace: Verifica que se puede crear y lanzar
        Devuelve: Nada
        """
        # crear la excepcion con un mensaje
        mensaje_prueba = "movimiento invalido"
        error = MovimientoInvalidoError(mensaje_prueba)
        
        # verificar que se creo
        resultado_none = (error == None)
        self.assertEqual(resultado_none, False)
        
        # verificar el mensaje
        mensaje_obtenido = str(error)
        self.assertEqual(mensaje_obtenido, "movimiento invalido")
        
        # probar lanzar la excepcion
        error_capturado = False
        try:
            raise MovimientoInvalidoError("no puedes mover")
        except MovimientoInvalidoError as e:
            error_capturado = True
            mensaje_error = str(e)
            self.assertEqual(mensaje_error, "no puedes mover")
        
        # verificar que se capturo el error
        self.assertEqual(error_capturado, True)
        
        # crear sin mensaje
        error2 = MovimientoInvalidoError()
        resultado_none2 = (error2 == None)
        self.assertEqual(resultado_none2, False)
        
        # verificar que hereda de BackgammonError
        es_backgammon = isinstance(error, BackgammonError)
        self.assertEqual(es_backgammon, True)
    
    def test_punto_invalido_error(self):
        """
        Prueba la excepcion PuntoInvalidoError.
        
        Recibe: Nada
        Hace: Verifica que se puede crear y lanzar
        Devuelve: Nada
        """
        # crear la excepcion con un mensaje
        mensaje_prueba = "punto invalido"
        error = PuntoInvalidoError(mensaje_prueba)
        
        # verificar que se creo
        resultado_none = (error == None)
        self.assertEqual(resultado_none, False)
        
        # verificar el mensaje
        mensaje_obtenido = str(error)
        self.assertEqual(mensaje_obtenido, "punto invalido")
        
        # probar lanzar la excepcion
        error_capturado = False
        try:
            raise PuntoInvalidoError("punto -1 no existe")
        except PuntoInvalidoError as e:
            error_capturado = True
            mensaje_error = str(e)
            self.assertEqual(mensaje_error, "punto -1 no existe")
        
        # verificar que se capturo el error
        self.assertEqual(error_capturado, True)
        
        # crear sin mensaje
        error2 = PuntoInvalidoError()
        resultado_none2 = (error2 == None)
        self.assertEqual(resultado_none2, False)
        
        # verificar que hereda de BackgammonError
        es_backgammon = isinstance(error, BackgammonError)
        self.assertEqual(es_backgammon, True)
    
    def test_valor_dado_invalido_error(self):
        """
        Prueba la excepcion ValorDadoInvalidoError.
        
        Recibe: Nada
        Hace: Verifica que se puede crear y lanzar
        Devuelve: Nada
        """
        # crear la excepcion con un mensaje
        mensaje_prueba = "dado invalido"
        error = ValorDadoInvalidoError(mensaje_prueba)
        
        # verificar que se creo
        resultado_none = (error == None)
        self.assertEqual(resultado_none, False)
        
        # verificar el mensaje
        mensaje_obtenido = str(error)
        self.assertEqual(mensaje_obtenido, "dado invalido")
        
        # probar lanzar la excepcion
        error_capturado = False
        try:
            raise ValorDadoInvalidoError("valor 8 no valido")
        except ValorDadoInvalidoError as e:
            error_capturado = True
            mensaje_error = str(e)
            self.assertEqual(mensaje_error, "valor 8 no valido")
        
        # verificar que se capturo el error
        self.assertEqual(error_capturado, True)
        
        # crear sin mensaje
        error2 = ValorDadoInvalidoError()
        resultado_none2 = (error2 == None)
        self.assertEqual(resultado_none2, False)
        
        # verificar que hereda de BackgammonError
        es_backgammon = isinstance(error, BackgammonError)
        self.assertEqual(es_backgammon, True)
    
    def test_juego_terminado_error(self):
        """
        Prueba la excepcion JuegoTerminadoError.
        
        Recibe: Nada
        Hace: Verifica que se puede crear y lanzar
        Devuelve: Nada
        """
        # crear la excepcion con un mensaje
        mensaje_prueba = "juego terminado"
        error = JuegoTerminadoError(mensaje_prueba)
        
        # verificar que se creo
        resultado_none = (error == None)
        self.assertEqual(resultado_none, False)
        
        # verificar el mensaje
        mensaje_obtenido = str(error)
        self.assertEqual(mensaje_obtenido, "juego terminado")
        
        # probar lanzar la excepcion
        error_capturado = False
        try:
            raise JuegoTerminadoError("ya hay ganador")
        except JuegoTerminadoError as e:
            error_capturado = True
            mensaje_error = str(e)
            self.assertEqual(mensaje_error, "ya hay ganador")
        
        # verificar que se capturo el error
        self.assertEqual(error_capturado, True)
        
        # crear sin mensaje
        error2 = JuegoTerminadoError()
        resultado_none2 = (error2 == None)
        self.assertEqual(resultado_none2, False)
        
        # verificar que hereda de BackgammonError
        es_backgammon = isinstance(error, BackgammonError)
        self.assertEqual(es_backgammon, True)
    
    def test_turno_incorrecto_error(self):
        """
        Prueba la excepcion TurnoIncorrectoError.
        
        Recibe: Nada
        Hace: Verifica que se puede crear y lanzar
        Devuelve: Nada
        """
        # crear la excepcion con un mensaje
        mensaje_prueba = "turno incorrecto"
        error = TurnoIncorrectoError(mensaje_prueba)
        
        # verificar que se creo
        resultado_none = (error == None)
        self.assertEqual(resultado_none, False)
        
        # verificar el mensaje
        mensaje_obtenido = str(error)
        self.assertEqual(mensaje_obtenido, "turno incorrecto")
        
        # probar lanzar la excepcion
        error_capturado = False
        try:
            raise TurnoIncorrectoError("no es tu turno")
        except TurnoIncorrectoError as e:
            error_capturado = True
            mensaje_error = str(e)
            self.assertEqual(mensaje_error, "no es tu turno")
        
        # verificar que se capturo el error
        self.assertEqual(error_capturado, True)
        
        # crear sin mensaje
        error2 = TurnoIncorrectoError()
        resultado_none2 = (error2 == None)
        self.assertEqual(resultado_none2, False)
        
        # verificar que hereda de BackgammonError
        es_backgammon = isinstance(error, BackgammonError)
        self.assertEqual(es_backgammon, True)
    
    def test_ficha_en_barra_error(self):
        """
        Prueba la excepcion FichaEnBarraError.
        
        Recibe: Nada
        Hace: Verifica que se puede crear y lanzar
        Devuelve: Nada
        """
        # crear la excepcion con un mensaje
        mensaje_prueba = "ficha en barra"
        error = FichaEnBarraError(mensaje_prueba)
        
        # verificar que se creo
        resultado_none = (error == None)
        self.assertEqual(resultado_none, False)
        
        # verificar el mensaje
        mensaje_obtenido = str(error)
        self.assertEqual(mensaje_obtenido, "ficha en barra")
        
        # probar lanzar la excepcion
        error_capturado = False
        try:
            raise FichaEnBarraError("mueve de la barra primero")
        except FichaEnBarraError as e:
            error_capturado = True
            mensaje_error = str(e)
            self.assertEqual(mensaje_error, "mueve de la barra primero")
        
        # verificar que se capturo el error
        self.assertEqual(error_capturado, True)
        
        # crear sin mensaje
        error2 = FichaEnBarraError()
        resultado_none2 = (error2 == None)
        self.assertEqual(resultado_none2, False)
        
        # verificar que hereda de BackgammonError
        es_backgammon = isinstance(error, BackgammonError)
        self.assertEqual(es_backgammon, True)
    
    def test_bear_off_invalido_error(self):
        """
        Prueba la excepcion BearOffInvalidoError.
        
        Recibe: Nada
        Hace: Verifica que se puede crear y lanzar
        Devuelve: Nada
        """
        # crear la excepcion con un mensaje
        mensaje_prueba = "bear off invalido"
        error = BearOffInvalidoError(mensaje_prueba)
        
        # verificar que se creo
        resultado_none = (error == None)
        self.assertEqual(resultado_none, False)
        
        # verificar el mensaje
        mensaje_obtenido = str(error)
        self.assertEqual(mensaje_obtenido, "bear off invalido")
        
        # probar lanzar la excepcion
        error_capturado = False
        try:
            raise BearOffInvalidoError("no puedes sacar fichas")
        except BearOffInvalidoError as e:
            error_capturado = True
            mensaje_error = str(e)
            self.assertEqual(mensaje_error, "no puedes sacar fichas")
        
        # verificar que se capturo el error
        self.assertEqual(error_capturado, True)
        
        # crear sin mensaje
        error2 = BearOffInvalidoError()
        resultado_none2 = (error2 == None)
        self.assertEqual(resultado_none2, False)
        
        # verificar que hereda de BackgammonError
        es_backgammon = isinstance(error, BackgammonError)
        self.assertEqual(es_backgammon, True)
    
    def test_herencia_correcta(self):
        """
        Prueba que todas las excepciones heredan correctamente.
        
        Recibe: Nada
        Hace: Verifica la jerarquia de herencia
        Devuelve: Nada
        """
        # BackgammonError hereda de Exception
        hereda_exception = issubclass(BackgammonError, Exception)
        self.assertEqual(hereda_exception, True)
        
        # MovimientoInvalidoError hereda de BackgammonError
        hereda1 = issubclass(MovimientoInvalidoError, BackgammonError)
        self.assertEqual(hereda1, True)
        
        # PuntoInvalidoError hereda de BackgammonError
        hereda2 = issubclass(PuntoInvalidoError, BackgammonError)
        self.assertEqual(hereda2, True)
        
        # ValorDadoInvalidoError hereda de BackgammonError
        hereda3 = issubclass(ValorDadoInvalidoError, BackgammonError)
        self.assertEqual(hereda3, True)
        
        # JuegoTerminadoError hereda de BackgammonError
        hereda4 = issubclass(JuegoTerminadoError, BackgammonError)
        self.assertEqual(hereda4, True)
        
        # TurnoIncorrectoError hereda de BackgammonError
        hereda5 = issubclass(TurnoIncorrectoError, BackgammonError)
        self.assertEqual(hereda5, True)
        
        # FichaEnBarraError hereda de BackgammonError
        hereda6 = issubclass(FichaEnBarraError, BackgammonError)
        self.assertEqual(hereda6, True)
        
        # BearOffInvalidoError hereda de BackgammonError
        hereda7 = issubclass(BearOffInvalidoError, BackgammonError)
        self.assertEqual(hereda7, True)
    
    def test_capturar_como_padre(self):
        """
        Prueba capturar excepciones hijas como padre.
        
        Recibe: Nada
        Hace: Verifica polimorfismo
        Devuelve: Nada
        """
        # capturar MovimientoInvalidoError como BackgammonError
        error_capturado = False
        try:
            raise MovimientoInvalidoError("test")
        except BackgammonError as e:
            error_capturado = True
            mensaje = str(e)
            self.assertEqual(mensaje, "test")
        
        self.assertEqual(error_capturado, True)
        
        # capturar PuntoInvalidoError como BackgammonError
        error_capturado2 = False
        try:
            raise PuntoInvalidoError("test2")
        except BackgammonError as e:
            error_capturado2 = True
            mensaje2 = str(e)
            self.assertEqual(mensaje2, "test2")
        
        self.assertEqual(error_capturado2, True)
        
        # capturar BearOffInvalidoError como Exception
        error_capturado3 = False
        try:
            raise BearOffInvalidoError("test3")
        except Exception as e:
            error_capturado3 = True
            mensaje3 = str(e)
            self.assertEqual(mensaje3, "test3")
        
        self.assertEqual(error_capturado3, True)
    
    def test_importar_todas(self):
        """
        Prueba importar todas las excepciones.
        
        Recibe: Nada
        Hace: Verifica que todas se pueden importar
        Devuelve: Nada
        """
        # verificar que BackgammonError existe
        existe1 = (BackgammonError == None)
        self.assertEqual(existe1, False)
        
        # verificar que MovimientoInvalidoError existe
        existe2 = (MovimientoInvalidoError == None)
        self.assertEqual(existe2, False)
        
        # verificar que PuntoInvalidoError existe
        existe3 = (PuntoInvalidoError == None)
        self.assertEqual(existe3, False)
        
        # verificar que ValorDadoInvalidoError existe
        existe4 = (ValorDadoInvalidoError == None)
        self.assertEqual(existe4, False)
        
        # verificar que JuegoTerminadoError existe
        existe5 = (JuegoTerminadoError == None)
        self.assertEqual(existe5, False)
        
        # verificar que TurnoIncorrectoError existe
        existe6 = (TurnoIncorrectoError == None)
        self.assertEqual(existe6, False)
        
        # verificar que FichaEnBarraError existe
        existe7 = (FichaEnBarraError == None)
        self.assertEqual(existe7, False)
        
        # verificar que BearOffInvalidoError existe
        existe8 = (BearOffInvalidoError == None)
        self.assertEqual(existe8, False)
    
    def test_comparacion_tipos(self):
        """
        Prueba comparacion de tipos de excepciones.
        
        Recibe: Nada
        Hace: Verifica que son tipos diferentes
        Devuelve: Nada
        """
        # crear dos excepciones diferentes
        error1 = MovimientoInvalidoError("test")
        error2 = PuntoInvalidoError("test")
        
        # obtener los tipos
        tipo1 = type(error1)
        tipo2 = type(error2)
        
        # verificar que son tipos diferentes
        son_diferentes = (tipo1 != tipo2)
        self.assertEqual(son_diferentes, True)
        
        # verificar que error1 es BackgammonError
        es_backgammon1 = isinstance(error1, BackgammonError)
        self.assertEqual(es_backgammon1, True)
        
        # verificar que error2 es BackgammonError
        es_backgammon2 = isinstance(error2, BackgammonError)
        self.assertEqual(es_backgammon2, True)


if __name__ == "__main__":
    unittest.main()