/*
Delaney Dow & Marlee Feltham
EC552 Spring 22 Final Project
*/

// https://github.com/marleef/EC552-Project.git
// g++ -o project project.cpp -std=c++17

#include <unordered_map>
#include <string>
#include <iostream>
#include <algorithm>
#include <fstream>
#include <vector>
#include <cstdlib> 

using namespace std;
#define COUNT 10 

std::ofstream outBest ("outBest.txt");
std::ofstream outWorst ("outWorst.txt"); 

/*
key: part
value: graph info (stages, steps, sharing)

hashMem:
{{'a', {stages, 1}, {steps, 1}}, {'ab', {stages, 2}, {steps, 2}}} => same as {{'a', grapha}, {'ab', graphab}}

graph:
{stages, 1}, {steps, 1}
*/

/* unordered map structs */
typedef unordered_map<string, int> graph;
typedef unordered_map<string, graph> hashGraph;

// global vector for printing and sending to GUI 
//std::vector<std::string> tree;  

// declare node class for Binary Search Tree Construction (& Printing) (for later use!!)
class Node {
    public: 
        Node* left; 
        char data; 
        Node* right; 

        Node(char d){
            data = d; 
            left = right = NULL; 
        }
}; 

/* print vals in hashGraph (nested map), used for debugging*/
void printhashGraph(hashGraph g)
{
    for (auto const &[x, y] : g)
    {
        cout << x << " : ";
        for (auto const &[x1, y1] : y)
        {
            if (&x1 != &y.begin()->first)
                cout << ", ";
            cout << x1 << " : " << y1;
        }
        cout << endl;
    }
}

/* combine child graphs */
graph combineGraphs(graph graphL, graph graphR)
{
    graph graphNew = graphL; // set graphNew as graphL
    graphNew.merge(graphR);  // merge graphL and graphR, set as graphNew

    graphNew["Stages"] = max(graphL["Stages"], graphR["Stages"]) + 1;
    graphNew["Steps"] = graphL["Steps"] + graphR["Steps"] + 1;

    return graphNew;
}

graph minCost(graph graph0, graph graph1)
{
    /* stages takes priority */
    if (graph0["Stages"] < graph1["Stages"])
    {
        return graph0;
    }
    else if (graph1["Stages"] < graph0["Stages"])
    {
        return graph1;
    }
    else if (graph0["Stages"] == graph1["Stages"])
    {
        /* stages are equal, check steps */
        if (graph0["Steps"] < graph1["Steps"])
        {
            return graph0;
        }
        else if (graph1["Steps"] < graph0["Steps"])
        {
            return graph1;
        }
    }
    return graph0; // arbitrarily choose graph0 if cost is equal
}

graph maxCost(graph graph0, graph graph1)
{
    /* stages takes priority */
    if (graph0["Stages"] > graph1["Stages"])
    {
        return graph0;
    }
    else if (graph1["Stages"] > graph0["Stages"])
    {
        return graph1;
    }
    else if (graph0["Stages"] == graph1["Stages"])
    {
        /* stages are equal, check steps */
        if (graph0["Steps"] > graph1["Steps"])
        {
            return graph0;
        }
        else if (graph1["Steps"] > graph0["Steps"])
        {
            return graph1;
        }
    }
    return graph0; // arbitrarily choose graph0 if cost is equal
}

/* graph building */
graph createAsmGraph(string part, hashGraph hashMem)
{
    if (hashMem.find(part) != hashMem.end())
    {
        // memoization case (memoization hash already has desired part)
        return hashMem[part]; // get graph part from hashMem
    }
    if (part.length() == 1)
    { // base case (part is primitive part)
        graph primitive;
        primitive["Stages"] = 0;
        primitive["Steps"] = 0;
        return primitive; // new graph with just the given part
    }
    /* initialization */
    graph graphL, graphR, graphBest, graphNew, graphWorst;
    string subpartL, subpartR;
    graphBest["Stages"] = 5000;
    graphBest["Steps"] = 5000;

    graphWorst["Stages"] = 1; 
    graphWorst["Steps"] = 1; 
    /* recursion */
    for (int i = 0; i < part.length() - 1; i++)
    {
        /* find best graph for L and R partitions */
        subpartL = part.substr(0, i + 1);
        subpartR = part.substr(i + 1, part.length());
        graphL = createAsmGraph(subpartL, hashMem);
        graphR = createAsmGraph(subpartR, hashMem);
        graphNew = combineGraphs(graphL, graphR); // make intermediate part
        graphBest = minCost(graphNew, graphBest); // save graph with best cost
        graphWorst = maxCost(graphNew, graphWorst); // save graph with worst cost 
    }
    pair<string, graph> new_elem(part, graphBest);
    hashMem.insert(new_elem); // add graph to hash table
    fstream fout;
    fout.open("export.csv", ios::out | ios::app);

    for (auto const &[x, y] : hashMem)
    {
        fout << x << " : ";
        for (auto const &[x1, y1] : y)
        {
            if (&x1 != &y.begin()->first)
                fout << ", ";
            fout << x1 << " : " << y1 << ",";
        }
        // fout << "\n";
    }
    return graphBest;
}

double calcCost(double cost_stage, double cost_step, graph out) {
    // define cost function as number of steps and stages and add them together 
    int stage = out["Stages"]; 
    int steps = out["Steps"]; 

    int cost; 
    cost = (cost_stage*stage) + (cost_step*steps); 
    return cost; 
}


//Construct BST from vector 
Node* createBST(vector<char> bst, int start, int end) {
    sort(bst.begin(), bst.end()); 

    // base case 
    if (start > end) {
        return NULL; 
    }

    // get middle element & make root 
    char mid = (start + end)/2; 
    Node* root = new Node(bst[mid]); 

    // recursively construct left subtree 
    root->left = createBST(bst, start, mid-1); 

    //recursively construct right subtree 
    root->right = createBST(bst, mid+1, end); 

    return root; 
} 

void print2DHelper (Node *root, int space) {
    // base case 
    if (root == NULL){
        return; 
    }

    // process right child
    space += COUNT; 
    print2DHelper(root->right, space); 

    // print node after space, count 
    outBest << " " << std:: endl; 
    for(int i = COUNT; i<space; i++) {
        outBest << " " << std::endl;  
    }
    outBest << root->data<< "\n" << std::endl; 

    // process left child 
    print2DHelper(root->left, space); 

    outBest.close();  
}

//print wrapper
void print2D(Node *root) {
    // pass initial space count as 0 
    print2DHelper(root, 0); 
}


 int main_interface(string part_file, double cost_stage, double cost_step)
{
    if (part_file.find(".csv") != false)
    {
        fstream fin;
        fin.open(part_file, ios::in);
    
        string line;
        hashGraph hashMem;
        graph out;
        double cost; 
        vector<char> bst; 
     
        while (!fin.eof())
        {
            fin >> line;
            line.erase(remove(line.begin(), line.end(), '.'), line.end());
            cout << "\n"  << line << endl;
            // send line to make a complete BST structure
            for (unsigned i - 0; i< line.length(); i++){
                char in = line[i]; 
                // insert into an array to use as keys 
                bst.push_back(in); 
            }
            hashMem.clear();
            out = createAsmGraph(line, hashMem); // return graph
            cost = calcCost(cost_stage, cost_step, out); // return cost of graph 
            for (const auto &x : out)
            {
                cout << x.first << ": " << x.second << endl;
            }
        }

        // send bst to create a binary search tree function 
        Node* root = createBST(bst, 0, bst.size() -1); 
        
        // printing and sending to GUI 
        print2D(root); 
    }

    return 0;
}
