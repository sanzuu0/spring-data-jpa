package com.szu.springdatajpa.entity;

import jakarta.persistence.*;
import lombok.*;
import lombok.experimental.FieldDefaults;

import java.util.List;

@Getter
@Setter
@Builder
@AllArgsConstructor
@NoArgsConstructor
@FieldDefaults(level = AccessLevel.PRIVATE)
@Table(name = "job", schema = "public", catalog = "data-jpa")
@Entity
public class JobEntity {
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Id
    @Column(name = "id", nullable = false)
    Long id;

    @Basic
    @Column(name = "company_name", nullable = false, length = 255)
    @Enumerated(EnumType.STRING)
    Company company;

    @Basic
    @Column(name = "experience", nullable = true, precision = 0)
    Double experience;

    @Basic
    @Column(name = "title", nullable = false, length = 500)
    String title;

    @Basic
    @Column(name = "max_salary", nullable = true)
    Integer maxSalary;

    @Basic
    @Column(name = "min_salary", nullable = true)
    Integer minSalary;

    @OneToMany(mappedBy = "job")
    @EqualsAndHashCode.Exclude
    @ToString.Exclude
    List<JobHistoryEntity> jobHistories;
}
