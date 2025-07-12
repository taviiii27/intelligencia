#include <iostream>
#include <cpr/cpr.h>
#include <nlohmann/json.hpp>
using namespace std;

int main() {
    nlohmann::json players = nlohmann::json::array({
        {
            {"name", "Alexandra"},
            {"age", 23},
            {"score", 400},
            {"level", 4}
        },
        {
            {"name", "Tavi"},
            {"age", 21},
            {"score", 1500},
            {"level", 19}
        }
    });

    cpr::Response res = cpr::Post(
        cpr::Url{"http://localhost:5000/game"},
        cpr::Body{players.dump()},
        cpr::Header{{"Content-Type", "application/json"}}
    );

    std::cout << "Status: " << res.status_code << "\n";
    std::cout << "Response: " << res.text << "\n";

    return 0;
}
