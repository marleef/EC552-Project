/*
Delaney Dow & Marlee Feltham
EC552 Spring 22 Final Project
*/

// https://github.com/marleef/EC552-Project.git
// g++ -o project project.cpp -std=c++17

#include <iostream>
#include <unordered_map>
#include <string>
#include <iostream>
#include <algorithm>

using namespace std;

// key: part
// value: graph info (stages, steps, sharing)

// #################### DATA PARSE #####################
typedef unordered_map<string, int> graph;
typedef unordered_map<string, graph> hashGraph;
// # create graph function

void printhashGraph(hashGraph g)
{
    for (auto const &[k1, v1] : g)
    {
        std::cout << k1 << " : ";
        for (auto const &[k2, v2] : v1)
        {
            if (&k2 != &v1.begin()->first)
                std::cout << ", ";
            std::cout << k2 << " : " << v2;
        }
        std::cout << std::endl;
    }
}

graph combineGraphs(graph graphL, graph graphR)
{
    graph graphNew = graphL;
    graphNew.merge(graphR);
    graphNew["Stages"] = max(graphL["Stages"], graphR["Stages"]) + 1;
    graphNew["Steps"] = graphL["Steps"] + graphR["Steps"] + 1;

    return graphNew;
}

graph minCost(graph graph0, graph graph1)
{
    if (graph0["Stages"] < graph0["Stages"])
    {
        return graph0;
    }
    else if (graph0["Stages"] > graph0["Stages"])
    {
        return graph1;
    }
    else if (graph0["Stages"] == graph0["Stages"])
    {
        if (graph0["Steps"] < graph0["Steps"])
        {
            return graph0;
        }
        else if (graph0["Steps"] > graph0["Steps"])
        {
            return graph1;
        }
    }

    return graph0;
}

graph createAsmGraph(string part, hashGraph hashMem)
{
    // printf("%lu\n", part.length());
    if (hashMem.find(part) != hashMem.end())
    {
        return hashMem[part];
    }
    if (part.length() == 1)
    {
        return hashMem[part];
    }

    graph graphL, graphR, graphBest, graphNew;
    string subpartL, subpartR;

    for (int i = 0; i < part.length() - 1; i++)
    {
        subpartL = part.substr(0, i + 1);
        subpartR = part.substr(i + 1, part.length());
        // cout << "subpartL " << subpartL << endl;
        // cout << "subpartR " << subpartR << endl;
        graphL = createAsmGraph(subpartL, hashMem);
        graphR = createAsmGraph(subpartR, hashMem);
        graphNew = combineGraphs(graphL, graphR);
        graphBest = minCost(graphNew, graphBest);
        // printf("%s", subpartL.c_str());
    }
    hashMem[part] = graphBest;
    for (const auto &x : hashMem[part])
    {
        std::cout << x.first << ": " << x.second << endl;
    }
    printhashGraph(hashMem);
    return hashMem[part];
}

int main()
{
    string part = "a.b.c.d";
    graph empty;
    empty["Stages"] = -1;
    empty["Steps"] = -1;
    empty["Sharing"] = -1;
    part.erase(std::remove(part.begin(), part.end(), '.'), part.end());
    hashGraph hashMem;
    // hashMem[] = empty;
    // for (const auto &x : empty)
    // {
    //     std::cout << x.first << ": " << x.second << endl;
    // }

    graph out = createAsmGraph("abcd", hashMem);
    // printf("%lu", part.length());
    // printhashGraph(hashMem);
}

/*
hashMem:
{{'a', {stages, 1}, {steps, 1}}, {'ab', {stages, 2}, {steps, 2}}} => same as {{'a', grapha}, {'ab', graphab}}

graph:
{stages, 1}, {steps, 1}
*/