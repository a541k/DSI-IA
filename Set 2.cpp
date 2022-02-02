#include<bits/stdc++.h>

using namespace std;

class consumable
{

    float total_time = 0, time_movie= 0, time_book = 0, time_series = 0;
    float rating = -1;
    string type, name;
    string start_date = "", end_date = "";
    int days_consumed = 0;

public:
    void add_consumable()
    {

        int type_choice;
        cout<<"Enter 1 for Book, 2 for Movie, 3 for Series\n";
        cin>>type_choice;
        type = (type_choice==1)? "Book":(type_choice==2)? "Movie": "Series";
        cout<<"selected type is "<<type;

        if(type == "Book"){

        }



    }

    void view_individual_list(){

    }

};

int main()
{
    int choice;
    string s = " Enter: 1. Add a consumable\n"
               "2. Edit a consumable\n"
               "3. Delete a consumable\n"
               "4. See the list of consumables and individually\n"
               "5. See overall info\n";

    cout<<s;
    cin>> choice;

    consumable c1;
    c1.add_consumable();


    return 0;


}
