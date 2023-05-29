from django.test import TestCase

from website.models import Benchmark
from django.contrib.auth.models import User


class BenchmarkTests(TestCase):
    """En esta clase van todas las pruebas del modelo Benchmark."""

    def test_creacion_benchmark(self):
        # caso uso esperado
        user_obj = User.objects.create(username="nombre_usuario", email="correo@example.com")
        benchmark = Benchmark(user=user_obj, type_analysis="Planning", country="Irlenad", industry="Automotive", credit_rating_borrower="A+", currency="EUR", principal="1,500,000", type_of_interest_rate="Float", base_rate="EURIBAR")
        benchmark.save()

        # Compruebo que el benchmark fue creado y la data fue guardad correctamente
        self.assertEqual(Benchmark.objects.count(), 1)
        self.assertEqual(benchmark.user, user_obj)
        self.assertEqual(benchmark.type_analysis, "Planning")
        self.assertEqual(benchmark.country, "Irlenad")
        self.assertEqual(benchmark.industry, "Automotive")
        self.assertEqual(benchmark.credit_rating_borrower, "A+")
        self.assertEqual(benchmark.currency, "EUR")
        self.assertEqual(benchmark.principal, "1,500,000")
        self.assertEqual(benchmark.type_of_interest_rate, "Float")
        self.assertEqual(benchmark.base_rate, "EURIBAR")

    def test_benchmark_str(self):
        user_obj = User.objects.create(username="nombre_usuario_2", email="correo_2@example.com")
        benchmark = Benchmark(user=user_obj, type_analysis="Planning", country="USA", industry="Security", credit_rating_borrower="AA", currency="EUR", principal="2,500,000", type_of_interest_rate="Float", base_rate="EURIBAR")
        benchmark.save()

        # Compruebo el str funciona como se desea
        self.assertEqual(benchmark.__str__(), "Planning, USA")