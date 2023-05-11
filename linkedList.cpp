#include <iostream>
#include <string>

struct Node {
    std::string url;
    Node* next;
};

class LinkedList {
public:
    LinkedList() : head(nullptr) {}

    void addNode(const std::string& url) {
        Node* newNode = new Node;
        newNode->url = url;
        newNode->next = nullptr;

        if (head == nullptr) {
            head = newNode;
        } else {
            Node* current = head;
            while (current->next != nullptr) {
                current = current->next;
            }
            current->next = newNode;
        }
    }

    void displayList() const {
        Node* current = head;
        while (current != nullptr) {
            std::cout << current->url << std::endl;
            current = current->next;
        }
    }

    ~LinkedList() {
        Node* current = head;
        while (current != nullptr) {
            Node* next = current->next;
            delete current;
            current = next;
        }
    }

private:
    Node* head;
};

int main() {
    LinkedList urlList;

    urlList.addNode("url1");
    urlList.addNode("url2");
    urlList.addNode("url3");
    urlList.addNode("url4");

    urlList.displayList();

    return 0;
}

