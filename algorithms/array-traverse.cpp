// This algorithm is Eridanoy's solution, who is a user on Codewars.
// Taken on 15.Jun.2021
// Slightly modified to suit my taste.
// Thank you for a great code!
#include <vector>

std::vector<int> snail(const std::vector<std::vector<int>>& arr)
{
  std::vector<int> ans = {};
  if(arr[0].empty()) return ans;
  int i = 0, k = 0, sz = arr.size(), y = 0;
  while(sz > 0) {
    while(k < sz) ans.push_back(arr[i][k++]); ++i; --k;
    while(i < sz) ans.push_back(arr[i++][k]); --i; --k;
    while(k >= y) ans.push_back(arr[i][k--]); --i; ++k; ++y;
    while(i >= y) ans.push_back(arr[i--][k]); ++i; ++k; --sz;
  }

  return ans;
}