#include<iostream>

int main()
{
  int num;
  std::cout<<"Enter a no.: ";
  std::cin>>num;
  for(int i=num;i>=1;i--)
  {
      for(int j=i;j>=1;j--)
    {
        std::cout<<"Kid ";
    }
    std::cout<<"\n";
  }
  return(0);
}
