#include <iostream>

int main ()
{
    static int array[10][10];
    int i, j, num1, num2, a;

    std::cout<<"Enter the order of the matix \n";

    std::cin>>num1;

    std::cin>>num2;

    if (num1 == num2)
    {
        std::cout<<"Enter the co-efficients of the matrix\n";

        for (i = 0; i < m; ++i)
        {
            for (j = 0; j < n; ++j)
            {
                std::cin>>array[i][j];
            }
        }

        std::cout<<"The matrix is \n";

        for (i = 0; i < m; ++i)
        {
            for (j = 0; j < n; ++j)
            {
                std::cout<<" "<<array[i][j];
            }
            std::cout<<"\n";
        }
        for (i = 0; i < m; ++i)
        {
            a = array[i][i];
            array[i][i] = array[i][m - i - 1];
            array[i][m - i - 1] = a;
        }

        std::cout<<"The matrix after changing the \n";

        std::cout<<"main diagonal & secondary diagonal\n";

        for (i = 0; i < m; ++i)
        {
            for (j = 0; j < n; ++j)
            {
                std::cout<<" "<<array[i][j];
            }
            std::cout<<"\n";
        }
    }
    else
        std::cout<<"The given order is not square matrix\n";
}