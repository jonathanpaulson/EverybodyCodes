#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <tuple>
#include <string>
#include <deque>
using namespace std;
using ll = int64_t;

int main() {
    vector<string> G;
    string row;
    while(cin) {
        cin >> row;
        G.push_back(row);
    }
    ll R = G.size();
    ll C = G[0].size();
    ll sr = -1;
    ll sc = -1;
    set<char> I;
    for(ll r=0; r<R; r++) {
        for(ll c=0; c<C; c++) {
            if(r==0 && G[r][c]=='.') {
                sr = r;
                sc = c;
            }
            if(G[r][c] != '#' && G[r][c]!='.' && G[r][c]!='~') {
                I.insert(G[r][c]);
            }
        }
    }
    map<char,int> item_to_idx;
    ll all_found = 0;
    ll idx = 0;
    for(auto& c : I) {
        item_to_idx[c] = idx;
        all_found |= 1<<idx;
        idx++;
    }

    deque<tuple<ll, ll, ll, ll>> Q;
    vector<int> SEEN(R*C*(all_found+1), false);
    //set<tuple<ll,ll,ll>> SEEN;
    Q.push_back(make_tuple(0, sr, sc, 0));
    cout << SEEN.size() << endl;
    ll count = 0;
    while(!Q.empty()) {
        auto [d,r,c,found] = Q.front();
        Q.pop_front();
        ll key = found*R*C + r*C + c;
        if(SEEN[key]) { continue; }
        SEEN[key] = true;
        count++;
        if(count % 1000000==0) {
            cout << count << endl;
        }
        if(r==sr && c==sc && found==all_found) {
            cout << d << endl;
            break;
        }
        for(auto [dr,dc] : vector<tuple<ll,ll>>{{-1,0},{1,0},{0,1},{0,-1}}) {
            ll rr = r+dr;
            ll cc = c+dc;
            if(0<=rr && rr<R && 0<=cc && cc<C && G[r][c]!='#' && G[r][c]!='~'){ 
                ll new_found = found;
                if(G[r][c] != '.') {
                    new_found |= (1<<item_to_idx[G[r][c]]);
                }
                Q.push_back(make_tuple(d+1, rr, cc, new_found));
            }
        }
    }
}
