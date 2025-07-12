#include <iostream>
#include <SFML/Graphics.hpp>

int main() {
    sf::RenderWindow window(sf::VideoMode({1000, 800}), "Intelligencia");
    sf::RectangleShape player(sf::Vector2f(100.f, 100.f)); /*dimension of pixels*/
    player.setFillColor(sf::Color::Red);
    player.setPosition(sf::Vector2f(350.f, 400.f));

    sf::Font font;
    if (!font.openFromFile("Super Adorable.ttf")) {
        std::cerr << "Eroare: nu s-a putut încărca fontul!\n";
        return 1;
    }

    sf::Text text(font, "scor: 1-0", 20);
    text.setFillColor(sf::Color::Red);

    while (window.isOpen()) {
        while (auto eventOpt = window.pollEvent()) {
            sf::Event event = *eventOpt;
            if (event.is<sf::Event::Closed>()) {
                window.close();
            }
        }

        window.clear();
        window.draw(player);
        window.draw(text);
        window.display();
    }

    return 0;
}
