package com.example.springbootapp;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@SpringBootApplication
public class SpringbootAppApplication {
    public static void main(String[] args) {
        SpringApplication.run(SpringbootAppApplication.class, args);
    }
}
@RestController
class HelloController {
    @GetMapping("/api")
    public String hello() {
        return "Hello, World!";
    }
}