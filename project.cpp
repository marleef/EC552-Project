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

using namespace std;

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
    graph graphL, graphR, graphBest, graphNew;
    string subpartL, subpartR;
    graphBest["Stages"] = 5000;
    graphBest["Steps"] = 5000;
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
    }
    pair<string, graph> new_elem(part, graphBest);
    hashMem.insert(new_elem); // add graph to hash table
    return graphBest;
}

int main()
{
    fstream fin;
    fin.open("dataset.csv", ios::in);
    string line;
    hashGraph hashMem;
    graph out;
    while (!fin.eof())
    {
        fin >> line;
        line.erase(remove(line.begin(), line.end(), '.'), line.end());
        cout << "\n"
             << line << endl;
        hashMem.clear();
        out = createAsmGraph(line, hashMem);
        for (const auto &x : out)
        {
            cout << x.first << ": " << x.second << endl;
        }
    }

    return 0;
}
