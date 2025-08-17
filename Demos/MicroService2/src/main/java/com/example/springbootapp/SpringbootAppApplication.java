package com.example.springbootapp;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.*;

@SpringBootApplication
public class SpringbootAppApplication {
    public static void main(String[] args) {
        SpringApplication.run(SpringbootAppApplication.class, args);
    }
}
@RestController
class MicroService1Controller {
    @GetMapping("/ms1")
    public String hello() {
        
    }
}

// @RestController
// @RequestMapping("/users")
// class UserController {
//     @Autowired
//     private UserRepository userRepository;

//     @PostMapping
//     public User createUser(@RequestBody User user) {
//         return userRepository.save(user);
//     }
// }