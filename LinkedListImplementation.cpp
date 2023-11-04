#include<iostream>
using namespace std;
class node{
    public:
        int data;
        node* next;
};
void insertAtEnd(node* &head)
{
    int val;
    node *n=new node();
    if(head==NULL)
    {
        head=n;
        head->data=val;
        head->next=NULL;
    }
    node *temp=head;
    while(temp->next!=NULL)
    {
        temp=temp->next;
    }
    temp->next=n;
    cout << "Enter the value you want to insert at end : ";
    cin >> val;
    n->data=val;
    n->next=NULL;
    
}

void insertAtBeg(node* &head)
{
    int val;
    node* n=new node();
    cout << "Enter the value you want to insert at beggining : ";
    cin >> val;
    n->data=val;
    n->next=head;
    head=n;

}

void insertAtPosition(node* &head)
{
    int val,pos,i=1;
    node* n=new node();
    node* temp=new node();
    temp=head;
    cout << "Enter the position at which you want to insert : ";
    cin >> pos;
    while(i<pos-1)
    {
        temp=temp->next;
        i++;
    }
    cout << "Enter the data you want to insert at position " << pos << " : ";
    cin >> val;
    n->data=val;
    n->next=temp->next;
    temp->next=n;

}

void deleteAtBeg(node* &head)
{
    node* temp=head;
    head=temp->next;
    delete temp;
}

void deleteAtEnd(node* &head)
{
    node* temp=head;
    while(temp->next->next!=NULL)
    {
        temp=temp->next;
    }
    delete temp->next;
    temp->next=NULL;
}

void deletePosition(node* &head)
{
    int delpos,j=1;
    node* temp=head;
    node* temp2=head;
    cout << "Enter the position of node you want to delete : ";
    cin >> delpos;
    if (delpos==1)
    {
        deleteAtBeg(head);
    }
    else
    {
    while(j<delpos-1)
    {
        temp=temp->next;
    }
    temp2=temp->next->next;
    delete temp->next;
    temp->next=temp2;
    }
}
void display(node* head)
{
    node* temp=new node();
    temp=head;
    while(temp!=NULL)
    {
        cout << temp->data << " -> " ;
        temp=temp->next;
    }
    cout << "NULL" << endl;
}
int main()
{
    int no,ch,a=1;
    node* head=NULL;
    cout << "\t\t\tSingly Linked List \n";
    cout << "Creating sample Linked List\n";
    cout << "Enter how many nodes you want in your sample Linked List : ";
    cin >> no;
    for(int i=0;i<no;i++)
    {
        insertAtEnd(head);
    }
    cout << "Created sample Linked List : ";
    display(head);
    while(a==1){
    cout << "\t\t\tMENU\t\t\t\n";
    cout << "1.Insert at Beggining\n";
    cout << "2.Insert at End\n";
    cout << "3.Insert at given position\n";
    cout << "4.Display Linked List\n";
    cout << "5.Delete Beggining node\n";
    cout << "6.Delete End node\n";
    cout << "7.Delete node at given position\n";
    cout << "8.Exit\n";
    cout << "Enter your choice : ";
    cin >> ch;
    switch (ch)
    {
        case 1:
            insertAtBeg(head);
            break;
        case 2:
            insertAtEnd(head);
            break;
        case 3:
            insertAtPosition(head);
            break;
        case 4:
            display(head);
            break;
        case 5:
            deleteAtBeg(head);
            break;
        case 6:
            deleteAtEnd(head);
            break;
        case 7:
            deletePosition(head);
            break;
        case 8:
            exit(0);
            break;
    }
    }
    return 0;
}
