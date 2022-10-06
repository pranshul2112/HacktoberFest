#include<iostream>

int main()
{
  int num,temp;
  std::cout<<"Enter the number your your choice: ";
  std::cin>>num;
  for(int i=1;i<11;i++)
  {
    temp=i*num;
    std::cout<<num<<"x"<<i<<"="<<temp<<std::endl;
  }
  return(0);
}
