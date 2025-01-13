#include <iostream>
#include <cmath> // Para fabs (valor absoluto de float)

using namespace std;

// Função que representa a equação f(x)
double f(double x) {
    return 5*x*x*x + x*x - 12*x + 4;
}

// Derivada da função f(x)
double f_prime(double x) {
    return 15*x*x + 2*x - 12;
}

// Função para o Método de Newton-Raphson
double newton_raphson(double (*f)(double), double (*f_prime)(double), double x0, double tol = 1e-7, int max_iter = 100) {
    double x = x0;
    for (int i = 0; i < max_iter; ++i) {
        double fx = f(x);
        double fpx = f_prime(x);
        
        // Imprime o erro atual e a derivada
        cout << "Iteração " << (i + 1) << ":" << endl;
        cout << "  x = " << x << endl;
        cout << "  f(x) = " << fx << endl;
        cout << "  f'(x) = " << fpx << endl;
        cout << "  Erro = " << fabs(fx) << endl;

        if (fpx == 0) {
            throw runtime_error("Derivada zero. O método falhou.");
        }
        
        double x_new = x - fx / fpx;
        
        if (fabs(x_new - x) < tol) {
            cout << "Convergência alcançada após " << (i + 1) << " iterações." << endl;
            return x_new;
        }
        
        x = x_new;
    }
    
    throw runtime_error("Número máximo de iterações atingido sem convergência.");
}

int main() {
    // Estimativa inicial
    double x0 = 1.0;
    
    try {
        // Encontrar a raiz
        double raiz = newton_raphson(f, f_prime, x0);
        cout << "A raiz encontrada é: " << raiz << endl;
    } catch (const runtime_error& e) {
        cerr << "Erro: " << e.what() << endl;
    }
    
    return 0;
}