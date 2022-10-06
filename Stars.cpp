#include<iostream>

int main()
{
  int num,temp;
  std::cout<<"Enter a no.: ";
  std::cin>>num;
  for(int i=1;i<=num;i++)
  {
      for(int j=1;j<=i;j++)
    {
        std::cout<<"*";
    }
    std::cout<<"\n";
  }
  return(0);
}
